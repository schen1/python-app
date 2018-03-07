# python-app

Creation of the project
```
oc new-project simple-deployment-scenario
```

Creation of the template
```
oc create -f template.yaml
```


Create the list of objects using default parameters in the template, does not create the template in OCP
```
oc process -f template.yaml | oc create -f -
```
Start the corresponding build for master branch
```
oc start-build bc/python-app-master
```

Create the list of objects overwritten default parameters in the template, does not create the template in OCP
```
oc process -f template.yaml -p GIT_REF=develop | oc create -f -
```


Delete the objects with label app=python-app-master
```
oc delete all -l app=python-app-master
```

Delete the objects with label app=python-app-develop
```
oc delete all -l app=python-app-develop
```
