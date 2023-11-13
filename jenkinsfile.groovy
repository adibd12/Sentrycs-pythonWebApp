pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Clone the GitHub repository
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']], 
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [[$class: 'CleanBeforeCheckout'], [$class: 'CloneOption', timeout: 60]],
                        userRemoteConfigs: [[url: 'https://github.com/adibd12/Sentrycs-pythonWebApp.git']]
                    ])
                }
            }
        }

        stage('Generate SSL Certificates') {
            steps {
                sh 'openssl req -x509 -nodes -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 365 -subj "/C=GB/ST=London/L=London/O=Alros/OU=IT Department/CN=localhost"'
            }
        }

        stage('Build Web App Docker Image') {
            steps {
                sh 'docker build . -t my_app'
            }
        }

        stage('Deploy application') {
            steps {
                sh 'docker-compose up'
            }
        }
    }
}
