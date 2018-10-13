if [ -n "$1" ]; then
    if [ $1 == 'run' ]; then 
        python3 manage.py runserver
    elif [ $1 == 'app' ]; then
        if [ -n "$2" ]; then
            echo "Creting '$2' app"
            python3 manage.py createapp $2
            echo 'Done'
            else
            echo "Please give a app name"
        fi
    elif [ $1 == 'mig' ]; then
        echo 'Doing Migrations'
        python3 manage.py migrate
    elif [ $1 == 'fmig' ]; then
        echo 'doing full migration'
        python3 manage.py makemigrations
        python3 manage.py migrate
    elif [ $1 == 'cmig' ]; then
        echo 'doing make migrations'
        python3 manage.py makemigrations
    elif [ $1 == 'git' ]; then
        echo 'Syning recent channges into github. Make SURE you tested the changes.'
        git status 
        read -p "PAK to add everything and commit"
        git add . 
        if [ -n "$2" ]; then
            git commit -m $2
            read -p "Commited"
            git push
            read -p "Pushed"
        else
            echo "Commit msg missing .. Use git commit_msg"
            fi
    fi
else
    echo ''
    echo 'Use the following command'
    echo ''
    echo 'run  - runserver'
    echo 'app  - createapp name_of_app'
    echo 'mig  - migrate'
    echo 'fmig - makemigrations then migrate'
    echo 'cmig - makemigrations only'
    echo 'git  - for syning to github.. Use git commit_msg'
fi