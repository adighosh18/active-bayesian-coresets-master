import pickle
import gzip
import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt


# with open("C:\Users\Adi\Desktop\ML Project\active-bayesian-coresets-master\experiments\experiments\active_torchvision\cifar10\acq_bald_cs_argmax_batch_100_labeled_1000_budget_10000_seed_222.pkl", 'rb') as f:
#     data = pickle.load(f)



with gzip.open("C:\Users\Adi\Desktop\ML Project\active-bayesian-coresets-master\experiments\experiments\
  active_torchvision\cifar10\acq_bald_cs_argmax_batch_100_labeled_1000_budget_10000_seed_222.pkl", 'rb') as f:
    train_set, valid_set, test_set = pickle.load(f)

train_x, train_y = train_set



plt.imshow(train_x[0].reshape((28, 28)), cmap=cm.Greys_r)
plt.show()