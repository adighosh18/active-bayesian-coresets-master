Method implemented is ..\torchvision_active_projections.py

Please run the main function in the file mentioned above.

You may also run through command line using command "Python torchvision_active_projections.py --dataset=dataset_name --budget=budget --batch_size=batch_size"
where dataset_name can be "cifar10", "cifar100", "mnist", "fashionmnist", "svhn" etc.

Default dataset used is MNIST.

Default number of testing data is 10,000 (which is whole dataset for MNIST).

Default budget is 1000.

Default batch construction method is the method implemented "FW" Active BALD Coreset Construction.

You may change these parameters in the code.

Library Environment requirements:

<ul>
  <li>Python >= 3.5</li>
  <li> torch >= 1.0 </li>
  <li>torchvision >= 0.2.2 </li>
  <li>numpy </li>
  <li>scipy </li>
  <li>sklearn </li>
  <li>pandas </li>
  <li>matplotlib </li>
  <li>gtimer
</ul>

Output is a .csv file named after dataset, stored in ..\experiments\projections\

It stores "number of queried datapoints", "accuracy" and "duration of iteration in seconds"
