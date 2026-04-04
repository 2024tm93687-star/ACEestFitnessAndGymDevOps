pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        // 1. Create venv 2. Upgrade pip 3. Install requirements
                        sh '''
                            python3 -m venv venv
                            ./venv/bin/python3 -m pip install --upgrade pip
                            ./venv/bin/python3 -m pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\python -m pip install --upgrade pip
                            venv\\Scripts\\python -m pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        // Use the python inside the venv to run pytest
                        sh './venv/bin/python3 -m pytest test_app.py -v'
                    } else {
                        bat 'venv\\Scripts\\python -m pytest test_app.py -v'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Docker commands are usually the same across platforms if Docker Desktop is installed
                    if (isUnix()) {
                        sh 'docker build -t aceest-fitness-app:latest .'
                    } else {
                        bat 'docker build -t aceest-fitness-app:latest .'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}