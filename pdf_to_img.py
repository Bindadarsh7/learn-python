from pdf2image import convert_from_path

old_pdf = convert_from_path("Concept of OOP.pdf",
                            poppler_path=r"C:\Users\binda\Desktop\pdf to image\poppler-22.11.0\Library\bin")
for i in range(len(old_pdf)):
    old_pdf[i].save("OOP"+str(i)+".jpg","JPEG")
print("Converted Successfuly")  