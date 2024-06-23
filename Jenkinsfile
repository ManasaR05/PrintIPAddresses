pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Replace with your actual Git repository URL
                git 'https://github.com/ManasaR05/PrintIPAddresses.git'
            }
        }
        stage('input1') {
            steps {
                sh "python ip_print.py input1.json"
            }
        }
        stage('input2') {
            steps {
                sh "python ip_print.py input2.json"
            }
        }
    }
}
