#!groovy
pipeline {
  agent none
  options {
    timestamps()
    skipStagesAfterUnstable()
  }
  stages {
    stage('Build') {
      agent any
      steps {
        sh '''#!/bin/bash
                echo "START"
                export WORKSPACE=`pwd`
                echo "START2"

                # Create/Activate virtualenv
                virtualenv venv
                echo "START3"
                source venv/bin/activate
                echo "START4"
                # Install Requirements
                pip install -r requirements.txt
                echo "START5"
                # Run tests
                python manage.py makemigrations
                echo "START6"
                python manage.py migrate
                echo "START7"
                python manage.py test
                echo "START8"
                '''
      }
    }
  }
  post {
    success {
      echo 'Build SUCCESS'
    }
  }
}