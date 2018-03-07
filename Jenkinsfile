properties(
    [
        pipelineTriggers([[$class: "SCMTrigger", scmpoll_spec: "H/12 * * * *"]])
    ]
)

node() {
	// define commands
	stage ('Start build') {
		checkout scm
		sh "oc start-build python-app-master"
	}
}