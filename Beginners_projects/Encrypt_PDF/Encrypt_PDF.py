import pikepdf

old_pdf = pikepdf.Pdf.open("Beginners_projects\Encrypt_PDF\AWT.pdf")

no_extr = pikepdf.Permissions(extract=False)

old_pdf.save("Beginners_projects\Encrypt_PDF\protect_new.pdf",
            encryption=pikepdf.Encryption(user="123456", owner="Meet", allow=no_extr))

