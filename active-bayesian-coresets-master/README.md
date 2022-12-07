Method implemented is ..\experiments\torchvision_active_projections.py

Please run the main function in the file mentioned above.

Default dataset used is MNIST.

Default number of testing data is 10,000 (which is whole dataset for MNIST).

Default budget is 1000.

Default batch construction method is the method implemented "FW" Active BALD Coreset Construction.

You may change these parameters in the code.

Library Environment requirements:

Python >= 3.5 torch >= 1.0 torchvision >= 0.2.2 numpy scipy sklearn pandas matplotlib gtimer

Output is a .csv file named after dataset, stored in ..\experiments\experiments\projections\

It stores "number of queried datapoints", "accuracy" and "duration of iteration in seconds"
