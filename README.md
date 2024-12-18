<div align=center>
  <h1><b>MaskSure</b></h1>
</div>

![](assets/20241128_214330_masksure.png)

<div align=center>
  Detecting Mask, Saving Lives.
</div>

## What's this?

<p align=justify>Hello! MaskSure is an amazing app that was created as a final project for the Computer Vision course. It's not just about doing an assignment; it's also a great opportunity to have some fun in the world of technology and to improve my portfolio!</p>

## Main goals

<p align=justify>It's a simple yet crucial feature that allows users to detect whether others are wearing masks or not. With the help of cutting-edge object detection technology, this application can ensure that everyone is following the rules and keeping our communities safe.</p>

<p align=justify>While it might not be perfect, like apps made by big companies, MaskSure is already an amazing achievement by a student.</p>

## Tech Stacks

To keep this app running smoothly, we use a few different technologies. Some of them are:

<ol><li align=justify><p>Streamlit</p>This is the foundation for creating and managing web app of Python, or the look and feel of the application. With Streamlit, we can build an interface that is straightforward but stylish enough for users. The app works great, and it's also visually appealing!</li><li align=justify><p>YOLO algorithm</p>YOLO is an amazing algorithm for object detection that is lightning fast and incredibly accurate. That means the MaskSure can instantly tell who is wearing a mask and who is not with just one look!</li><li align=justify><p>Pillow (PIL)</p>When it comes to images, we use Pillow. This library helps with simple image processing, such as resizing, and makes it easier for the app to handle images.</li></ol>

## Installation

To use this application, you need to do a few things to make it work:

#### 1. Clone this repository

```bash
git clone https://github.com/ramadityo/masksure.git
```

#### 2. Add python env to the app folder

For Windows:

```bash
py -m venv .venv
```

```bash
.venv\Scripts\activate
```

For Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

#### 3. Install libraries from requirements.txt

```bash
pip3 install -r requirements.txt
```

#### 4. Run the app

```bash
streamlit run app.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/MIT) link for details.
