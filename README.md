# Breast_Cancer_Classification

**Breast cancer classification on Keras** (based on the implementaion of CancerNet algorithm by Adrian Rosebrock on pyimageseach).

Breast cancer is the most common form of cancer in women, and invasive ductal carcinoma (IDC) is the most common form of breast cancer. Accurately identifying and categorizing breast cancer subtypes is an important clinical task, and automated methods can be used to save time and reduce error.

The goal of this script is to identify IDC when it is present in otherwise unlabeled histopathology images.
The dataset consists of 277,524 50x50 pixel RGB digital image patches that were derived from 162 H&E-stained breast histopathology samples.
These images are small patches that were extracted from digital images of breast tissue samples. 
The breast tissue contains many cells but only some of them are cancerous. 
Patches that are labeled "1" contain cells that are characteristic of invasive ductal carcinoma. 
For more information about the data, 
see https://www.ncbi.nlm.nih.gov/pubmed/27563488 and http://spie.org/Publications/Proceedings/Paper/10.1117/12.2043872.
