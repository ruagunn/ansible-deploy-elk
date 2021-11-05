pipeline {
    agent any

    stages {
        
        stage('Install packages') {
            steps {
                ansiblePlaybook( 
                    playbook: 'packages.yml',
					inventory: "inventory"
                )
            }
        }
        stage('Infrastructure Test') {
            steps {
                sh '''#!/bin/bash
                    py.test-3 -v tests/infrastructure/test_packages.py
                    py.test-3 -v tests/infrastructure/test_services.py
                '''
            }
        }
        stage('Functional Test') {
            steps {
                sh '''#!/bin/bash
                    py.test-3 -v tests/functional/test_functional.py
                '''
            }
        }
        stage('Integration Test') {
            steps {
                sh '''#!/bin/bash
                    py.test-3 -v tests/integration/test_integration.py
                '''
            }
        }
        stage('Performance Test') {
            steps {
                sh '''#!/bin/bash
                    py.test-3 -v tests/performance/test_performance.py
                '''
            }
        }
        stage('SonarQube Static Code Analysis') {
            steps {
                
                sh '''#!/bin/bash
                    /opt/sonar-scanner/bin/sonar-scanner \
                        -Dsonar.projectKey=python \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.login=ccaf405da010b74c772732b95b275534ffd8c77f
                '''
            }
        }
        stage('Clean old ELK stack') {
            steps {
                ansiblePlaybook( 
                    playbook: 'elk-clean.yml',
					inventory: "inventory"
                )
            }
        }
		stage('Deploy ELK stack') {
            steps {
                ansiblePlaybook( 
                    playbook: 'elk.yml',
					inventory: "inventory"
                )
            }
        }
    }
}