
#!/bin/bash

# project directory
PROJECT_DIR= "D:/jobs/DATA_SHOW"


# check if the venv exists
# replace with your own path
if [ ! -d $PROJECT_DIR ]; then
    echo "Creating virtual environment..."
    cd $PROJECT_DIR
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    deactivate
fi

# create reuirements.txt
function create_dependencies() {
    echo "Creating requirements.txt..."
    cd $PROJECT_DIR
    python3 -m pip freeze > requirements.txt
}


# start the server
function start() {
    echo "Starting server..."
    cd $PROJECT_DIR
    source venv/bin/activate
    python3 server.py &
    deactivate
}

# stop the server
function stop() {
    echo "Stopping server..."
    sudo kill -9 $(ps aux | grep '[p]ython3 server.py' | awk '{print $2}')
}


# create database statistics in mysql if not exists
function create_database() {
    echo "Creating database..."
    mysql -u root -p < $PROJECT_DIR/create_database.sql
}

# init project
function init() {
    create_database
    create_dependencies
    start
}

# push code to github
function push() {
    echo "Pushing code to github..."
    cd $PROJECT_DIR
    git add .
    git commit -m "update"
    git push origin master
}


# restart the server
function restart() {
    stop
    start
}

# add create requirements.txt to start
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    init)
        init
        ;;
    restart)
        restart
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|init}"
        exit 1
        ;;
esac

exit 0