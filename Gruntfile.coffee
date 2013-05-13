module.exports = (grunt) ->
	# Project configuration
	grunt.initConfig(
		pkg : grunt.file.readJSON('package.json')
		cssmin:
			compress:
				files:
					'app/static/css/woojuu.min.css': ['app/static/css/woojuu.css']
					'app/static/css/normalize.min.css': ['app/static/css/normalize.css']
	)

	# Load the plugins that provide tasks
	grunt.loadNpmTasks('grunt-contrib-cssmin')

	# Default task
	grunt.registerTask 'default', ['cssmin']