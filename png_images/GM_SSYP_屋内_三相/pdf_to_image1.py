import os
import fitz
for f in os.listdir('./'):
    if ".pdf" in f:
        #pdf_path = os.path.join(dir_path,f)
        print(f)
        pdf_name=f.split('.')[0]
        doc = fitz.open(f)
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG('%s.png' % pdf_name)