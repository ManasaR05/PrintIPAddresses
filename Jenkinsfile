pipeline {
    agent any
    // Defines the stages of the pipeline
    stages {
        //Stage 1: Checks out the code from the main branch of the mentioned GitHub repository
        stage('Checkout to main') {
            steps {
                git branch: 'main', url: 'https://github.com/ManasaR05/PrintIPAddresses.git'
            }
        }
        // Stage 2: Creating a Python virtual environment
        stage('Creating virtual environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        // Stage 3: Installing the Python packages from requirements.txt
        stage('Installing requirements') {
            steps {
                sh '''
                source venv/bin/activate
                pip3 install -r requirements.txt
                '''
            }
        }
        // Stage 4: Runs the Python script with two different input files
        stage('run codes in console with input files') {
            steps {
                sh '''
                source venv/bin/activate
                python3 ip_print.py input1.json
                python3 ip_print.py input2.json
                '''
            }
        }
        // Stage 5: Execution of the Robot Framework test suite
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
