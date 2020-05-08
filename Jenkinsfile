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
    stage('Generate Documents') {
      steps {
        sh """
          source ./.env/bin/activate
          pip list
          pydocmd build
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
    stage('Verify Local Install') {
      steps {
        sh """
          source ./.env/bin/activate
          python -m pip install ./
          """
      }
    }
    stage('Sonar Analysis') {
      steps {
        stepPythonSonarAnalysis()
      }
    }
    stage('Publish Package') {
      when { expression { return env.LS_GIT_BRANCH ==~ "release.*" } }
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
