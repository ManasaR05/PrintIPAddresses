pipeline {
    agent any
    stages {
        stage('Checkout to main') {
            steps {
                git branch: 'main', url: 'https://github.com/ManasaR05/PrintIPAddresses.git'
            }
        }
        stage('Creating virtual environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Installing requirements') {
            steps {
                sh '''
                source venv/bin/activate
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('run codes in console with input files') {
            steps {
                sh '''
                source venv/bin/activate
                python3 ip_print.py input1.json
                python3 ip_print.py input2.json
                '''
            }
        }

        stage('Running robot test') {
            steps {
                sh '''
                source venv/bin/activate
                robot test.robot
                '''
            }
        }
    }
}
