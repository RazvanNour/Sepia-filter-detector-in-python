import extcolors
#IMAGINI NORMALE
colorsn1, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n1.jpg")
colorsn2, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n2.jpg")
colorsn3, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n3.jpg")
colorsn4, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n4.jpg")
colorsn5, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n5.jpg")
colorsn6, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n6.jpg")
colorsn7, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n7.jpg")
colorsn8, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n9.jpg")
colorsn9, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/n10.jpg")



colorss1, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s1.jpg")
colorss2, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s2.jpg")
colorss3, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s3.jpg")
colorss4, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s4.jpg")
colorss5, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s5.jpg")
colorss6, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s6.jpg")
colorss7, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s7.jpg")
colorss8, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s8.jpg")
colorss9, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s9.jpg")
colorss10, pixel_count = extcolors.extract("C:/Users/PycharmProjects/LAB10/Imagini/s10.jpg")

def averageRed(colors): #
    x=0
    s=0
    for i in range(0,min(5,len(colors))):
        for j in range(0,3):
            s = s + colors[i][0][j]
        x = x + colors[i][0][0] / s
    x = x / len(colors)
    return x
#R/R+G+B
f = open("sepia.data", "w")
lineoftext = [len(colorsn1),averageRed(colorsn1),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn2),averageRed(colorsn2),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn3),averageRed(colorsn3),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn4),averageRed(colorsn4),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn5),averageRed(colorsn5),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn6),averageRed(colorsn6),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn7),averageRed(colorsn7),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn8),averageRed(colorsn9),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorsn9),averageRed(colorsn10),0]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss1),averageRed(colorss1),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss2),averageRed(colorss2),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss3),averageRed(colorss3),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss4),averageRed(colorss4),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss5),averageRed(colorss5),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss6),averageRed(colorss6),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss7),averageRed(colorss7),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss8),averageRed(colorss8),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss9),averageRed(colorss9),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

lineoftext = [len(colorss10),averageRed(colorss10),1]
f.write(str(lineoftext).strip('[]'))
f.write("\n")

f.close()