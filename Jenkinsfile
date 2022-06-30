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
        sh deploy.sh
      }
    }
  }
  post {
    success {
      echo 'Build SUCCESS'
    }
  }
}