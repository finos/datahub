pipeline {
  agent { label 'python36' }
  options { timeout(time: 20, unit: 'MINUTES') }
  stages {
    stage('Initialise') {
      steps {
        stepInitialise()
        stepPythonConfigure()
      }
    }
    stage('Install Dependencies') {
      steps {
        sh """
          python -m venv .env
          source ./.env/bin/activate
          python -m pip install -r requirements.txt
          python -m pip install pytest pytest-cov coverage
          """
      }
    }
    stage('Unit Tests') {
      steps {
        sh """
          source ./.env/bin/activate
          python -m pytest --cov-report xml --cov=. --junitxml=test_results.xml ./tests
          """
      }
    }
    stage('Sonar Analysis') {
      steps {
        stepPythonSonarAnalysis()
      }
    }
    stage('Publish Package') {
      steps {
        stepPythonPackagePublish()
      }
    }
  }
  post {
    always {
      stepFinalise()
    }
  }
}
