import PyPDF2
import pandas as pd


def pdf_to_txt(page_number):
	pdf_file = open("./gradePDF/grd20221EN.pdf", "rb")
	reader = PyPDF2.PdfFileReader(pdf_file)

	page = reader.getPage(page_number)
	text = page.extract_text()

	txt_file = open("./gradePDF/grd20221EN.txt", "w")
	txt_file.writelines(text)

	txt_file.close()
	pdf_file.close()
	return reader.numPages


def open_files():
	engineering_department = ["AERO", "BMEN", "BIOT", "CHEN", "SENG", "CVEN", "EVEN", "CLEN", "CYBR", "ENGR", "ICPE",
	                          "CSCE", "ECEN", "ESET", "IDIS", "MMET", "MXET", "TCMT", "ISEN", "MSEN", "MEEN", "AREN",
	                          "ITDE", "NUEN", "OCEN", "PETE"]
	csce = []
	csce_course = []
	csce_course_section = []
	grade_format = {
		'a': "",
		'b': "",
		'c': "",
		'd': "",
		'f': "",
		'a-f': "",
		'i': "",
		's': "",
		'u': "",
		'q': "",
		'x': "",
		'total': "",
		'professor': "",
	}

	total_page_num = pdf_to_txt(0)  # convert pdf to txt file
	line_start = 21
	section_increment = 6

	for i in range(total_page_num-1):
		read_txt_file = open("./gradePDF/grd20221EN.txt", "r")
		lines = read_txt_file.readlines()[line_start:]
		for line in lines:
			print(line.strip().split())

		pdf_to_txt(i+1)
		read_txt_file.close()



def main():
	open_files()


if __name__ == "__main__":
	main()
