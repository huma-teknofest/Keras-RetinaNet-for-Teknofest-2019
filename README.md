<p align="center"><img src="https://github.com/huma-teknofest/huma-teknofest.github.io/blob/master/assets/images/huma-transparent.png" /></p>

<h1 align="center">Keras RetinaNet for Teknofest 2019 AI Competition</h1>
<p>Using RetinaNet for object detection from drone images in Teknofest istanbul 2019 Artificial Intelligence Competition</p>


### :rocket: Teknofest 2019 - Yapay Zeka Yarışması:
TEKNOFEST 2019 Yapay Zeka Yarışması kapsamında takımlar bir drone ile önceden kaydedilmiş görüntüler üzerinden verilen süre içerisinde araç ve insan tespitini özel bir metrik üzerinden IoU puanı ile puanlandırılmıştır.

<h2 align="center">:books: Öğretici Döküman (Tutorial)</h2>

Keras RetinaNet kurulum ve kendi veri kümenizi eğitmek ve test etmek için detaylı öğretici dökümanını [buradan](https://medium.com/@sddkal/keras-retinanet-d588f87b0350) inceleyebilirsiniz.




<h2 align="center">:clipboard: Başlangıç Kılavuzu (Getting Started)</h2>

### :floppy_disk: Ön Koşullar (Software Prerequisites)
- cython
- pycocotools==2.0.0
- keras-resnet==0.2.0
- h5py==2.10.0
- keras==2.4.3
- matplotlib
- numpy==1.19.5
- six==1.15.0
- opencv-python==3.4.13.47
- pillow
- progressbar2
- tensorflow-gpu==2.4.1
- git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI
- tqdm

### Kurulum
Python 3.7 kurulum ve virtual env oluşturma 

- `sudo apt install python3.7 python3-venv python3.7-venv`

- `sudo apt-get install python3.7-dev`

- `python3.7 -m venv .py37-venv`

- `source .py37-venv/bin/activate`

Ön koşullu paketlerin kurulumu

- `pip3 install cython`

- `pip3 install numpy==1.19.5`

- `pip3 install -r requirements.txt`

keras_retinanet kütüphanesinin derlenmesi

- `pip3 install .`

- `python3 setup.py build_ext --inplace`

### :blue_book: Klasör Yapısı (Folder Structure)

```
main_dir
- dataset_test
- retinanet
    - keras_retinanet
    - models
        - teknofest19_huma_resnet50_21_37_inference.h5
    - snapshots
        - teknofest19_huma_resnet50_21_37_ss.h5
    - results
    - detect_all_images.py
```

<h2 align="center">:hourglass: Eğitim (Train)</h2>

RetinaNet'in Keras implementasyonuna ve eğitim dökümanına [buradan](https://github.com/fizyr/keras-retinanet) ulaşabilirsiniz.

Drone ile çekilmiş yaklaşık 30bin görüntü üzerinden etiketlenmiş araç ve insan veri kümesi ile 58 epoch eğitilmiş ResNet-50 RetinaNet snapshot dosyasını [buradan](https://drive.google.com/open?id=1TUQCY4dHaW2YZ6ymNyk9PsDbJQsm0xJR) indirebilirsiniz.


<h2 align="center">:watch: Test</h2>

Önceden eğitilmiş ve dönüştürülmüş model dosyası olan ```teknofest19_huma_resnet50_21_37_inference.h5``` dosyasını [buradan](https://drive.google.com/open?id=1TUQCY4dHaW2YZ6ymNyk9PsDbJQsm0xJR) indirerek retinanet klasörü altında models klasörü altına kopyalayınız.

Test yapabilmeniz için örnek test görüntülerini [buradan](https://drive.google.com/open?id=1Pfjk-YS2-GPd-JxuXHgk2DAHjD05Tamx) indererek ```dataset_test``` klasörü altına kopyalayınız.

Eğitilmiş model ile ```dataset_test``` klasöründeki resimler üzerinde nesne tespiti yapmak için ```detect_all_images.py``` python programını çalıştırabilirsiniz.
Tahmin (prediction) sonuçlarını ```results``` klasörü altına resmin üzerine çizilmiş şekilde çıkartılacaktır.

<h2 align="center">:tada: Sonuçlar (Results)</h2>
<p align="center"><img width="100%" src="retinanet/results/results.gif" /></p>

<h2 align="center">:satellite: Contact (İletişim)</h2>

* :globe_with_meridians: [Takım Web Sitesi](https://huma-teknofest.github.io/)
* :mailbox: [E-posta Adresi](huma.teknofest@gmail.com)
