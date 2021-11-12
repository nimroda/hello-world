node {
    def app
    def job

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("hello_world")
    }
    
    stage('Deploy Container') {
        build job: 'ansible-docker'
    }
    
    stage('Bye') {
        echo "Bye bye!"
    }
    
}
