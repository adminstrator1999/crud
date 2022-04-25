pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'echo "Hello world!"'
                sh '''
                    echo "Multi shell step works too"
                    ls -lah
                '''
            }
        }
    }
}