pipeline {
    agent any

    stages {
        stage('Fetch repo') {
            steps {
                echo 'Git fetch'
                git url: 'https://github.com/borisbaldassari/ggi-webapp.git'
            }
        }
        stage('Fetch activities') {
            steps {
                echo 'Fetch activities..'
                sh '''
#export PATH=/var/lib/jenkins/.local/bin:$PATH
cd scripts && python3.9 get_activities.py
                '''
            }
        }
        stage('Build webapp') {
            steps {
                echo 'Build website..'
                sh '''
cd webapp && hugo -D 
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh '''
rm -rf /var/www/html/ggi-webapp/*
cp -r webapp/public/* /var/www/html/ggi-webapp/
                '''
            }
        }
    }
}

