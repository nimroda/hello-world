node {
    def app
    def job

    stage('Clone repository') {
        checkout scm
    }

    stage('Build hello-world image') {
        app = docker.build("hello_world")
    }
    
    stage('Triggering ansible-docker job to deploy the container') {
        build job: 'ansible-docker'
    }
}
