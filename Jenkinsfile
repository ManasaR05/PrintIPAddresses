pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Git repository URL
                git 'https://github.com/ManasaR05/PrintIPAddresses.git'
            }
        }
        stage('input1') {
            steps {
                sh "python3 ip_print.py input1.json"
            }
        }
        stage('input2') {
            steps {
                sh "python3 ip_print.py input2.json"
            }
        }
        stage('robot_test') {
            steps {
                sh "robot test.robot"
            }
        }
    }
}
