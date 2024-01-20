from PIL import Image

def juntar_redimensionar_imagens(imagem1_path, imagem2_path, largura, altura, saida_path):
    # Abre as imagens
	imagem1 = Image.open(imagem1_path)
	imagem2 = Image.open(imagem2_path)

    # Redimensiona as imagens
	imagem1 = imagem1.resize((1280, 420))
	
    # calc 
	larg = imagem2.size[0]
	newLarg = 300 / imagem2.size[1]
	newSize = (int(larg * newLarg), 300)
	imagem2 = imagem2.resize(newSize)
	pos = (imagem2.size[0] - 1280)
    # Junta as imagens horizontalmente
	imagem_junta = Image.new('RGB', (largura, altura))
	imagem_junta.paste(imagem1, (0, 0))
	imagem_junta.paste(imagem2, (-pos, 420))

    # Salva a imagem resultante
	imagem_junta.save(saida_path)

# Exemplo de uso
juntar_redimensionar_imagens('imagem1.jpg', 'imagem2.jpg', 1280, 720, 'saida.jpg')

