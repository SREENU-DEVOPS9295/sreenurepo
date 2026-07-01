- task: PythonScript@0
 inputs:
   scriptSource: 'filePath'
   scriptPath: 'scripts/deploy.py'
   workingDirectory: '$(Build.SourcesDirectory)/scripts'
   failOnStderr: true
   test
