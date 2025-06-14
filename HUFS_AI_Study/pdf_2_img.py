import fitz  # PyMuPDF
import os

pdf_path = '컴비_기말.pdf'
output_folder = 'pdf_images'
os.makedirs(output_folder, exist_ok=True)

# PDF 파일 열기
doc = fitz.open(pdf_path)

# 각 페이지를 이미지로 저장
for page_number in range(len(doc)):
    page = doc.load_page(page_number)                          # 페이지 로드
    pix = page.get_pixmap(dpi=300)                             # 렌더링 해상도 설정
    image_path = os.path.join(output_folder, f'page_{page_number + 1}.png')
    pix.save(image_path)                                       # 이미지 저장

print(f"총 {len(doc)} 페이지가 이미지로 저장되었습니다.")
