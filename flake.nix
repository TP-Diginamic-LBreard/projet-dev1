{
  description = "Python environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs {
            inherit system;
          };
          pythonEnv = pkgs.python312.withPackages(ps: with ps; [
            fastapi
            pymysql
            python-dotenv
            sqlalchemy
            uvicorn
          ]);
        in
        {
          devShells.default = pkgs.mkShell {
            packages = with pkgs; [
              pythonEnv
              mariadb
            ];

            # https://jeancharles.quillet.org/posts/2022-01-30-Local-mariadb-server-with-nix-shell.html
            shellHook = ''
              MYSQL_BASEDIR=${pkgs.mariadb}
              MYSQL_HOME="$PWD/mysql"
              MYSQL_DATADIR="$MYSQL_HOME/data"
              export MYSQL_UNIX_PORT="$MYSQL_HOME/mysql.sock"
              MYSQL_PID_FILE="$MYSQL_HOME/mysql.pid"
              alias mysql='mysql -u root'

              if [ ! -d "$MYSQL_HOME" ]; then
                # Make sure to use normal authentication method otherwise we can only
                # connect with unix account. But users do not actually exists in nix.
                mysql_install_db --no-defaults --auth-root-authentication-method=normal \
                  --datadir="$MYSQL_DATADIR" --basedir="$MYSQL_BASEDIR" \
                  --pid-file="$MYSQL_PID_FILE"
              fi

              # Starts the daemon
              # - Don't load mariadb global defaults in /etc with `--no-defaults`
              # - Disable networking with `--skip-networking` and only use the socket so 
              #   multiple instances can run at once
              mysqld --no-defaults --skip-networking --datadir="$MYSQL_DATADIR" --pid-file="$MYSQL_PID_FILE" \
                --socket="$MYSQL_UNIX_PORT" 2> "$MYSQL_HOME/mysql.log" &
              MYSQL_PID=$!

              finish()
              {
                mysqladmin -u root --socket="$MYSQL_UNIX_PORT" shutdown
                kill $MYSQL_PID
                wait $MYSQL_PID
              }
              trap finish EXIT
            '';
          };
        }
      );
}
