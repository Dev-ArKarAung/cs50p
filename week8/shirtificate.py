import fpdf

def main():
    name = input("Name: ")

    pdf = fpdf.FPDF(orientation="P", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", style="B", size=24)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    image_width = 120
    x = (210 - image_width) / 2
    pdf.image("shirtificate.png", x=x, y=40, w=image_width)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", style="B", size=18)
    pdf.set_xy(10, 75)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()