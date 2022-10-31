from chip.demoTest import demoTest


def chinaPaint(imgname):
    imgFile = "static\\image\\" + imgname
    model_name="dataset1"
    input_name=imgname
    global onshow_path
    demoTest(model_name, imgFile, input_name,10)


