import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_edges(image):
    # Aplica a transformada de Canny para detectar as bordas na imagem
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    return edges

def detect_lines(edges):
    # Aplica a transformada de Hough para detectar as linhas nas bordas da imagem
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=20, maxLineGap=5)
    return lines

def classify_edges(lines):
    # Classifica cada linha como degrau, rampa ou telhado
    examples = {
        "degrau": [],
        "rampa": [],
        "telhado": []
    }
    
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i, 0]
        line_profile = []
        
        # Calcula o perfil da linha
        if abs(x2 - x1) > abs(y2 - y1):
            # A linha é horizontal
            for x in range(min(x1, x2), max(x1, x2) + 1):
                y = int((y2 - y1) / (x2 - x1) * (x - x1) + y1)
                line_profile.append(image[y, x])
        else:
            # A linha é vertical
            for y in range(min(y1, y2), max(y1, y2) + 1):
                x = int((x2 - x1) / (y2 - y1) * (y - y1) + x1)
                line_profile.append(image[y, x])
        
        # Verifica o tipo de borda
        if np.var(line_profile) < 100:
            # A linha é um degrau
            examples["degrau"].append((x1, y1, x2, y2, line_profile))
        else:
            # A linha é uma rampa ou um telhado
            # Verifica se há uma rampa de cada lado da linha
            left_profile = line_profile[:len(line_profile)//2]
            right_profile = line_profile[len(line_profile)//2:]
            left_var = np.var(left_profile)
            right_var = np.var(right_profile)
            if left_var < 100 and right_var >= 100:
                # A linha é uma rampa à direita
                examples["rampa"].append((x1, y1, x2, y2, line_profile))
            elif left_var >= 100 and right_var < 100:
                # A linha é uma rampa à esquerda
                examples["rampa"].append((x1, y1, x2, y2, line_profile))
            elif left_var >= 100 and right_var >= 100:
                # A linha é um telhado
                examples["telhado"].append((x1, y1, x2, y2, line_profile))
    
    return examples

def plot_line_profiles(examples, edge_type):
    # Plota o perfil de cada linha do tipo especificado
    for i in range(12, 13):
        x1, y1, x2, y2, line_profile = examples[edge_type][i]
        plt.plot(line_profile, label=f"Linha {i+1}")
    plt.title(f"Exemplos de bordas do tipo '{edge_type}'")
    plt.xlabel("Distância ao longo da linha")
    plt.ylabel("Intensidade de pixel")
    plt.legend()
    plt.show()

# Carrega a imagem
image = cv2.imread("Fig1026(a)(headCT-Vandy).png", cv2.IMREAD_GRAYSCALE)

# Detecta as bordas e as linhas
edges = detect_edges(image)
lines = detect_lines(edges)

# Classifica as bordas em degrau, rampa ou telhado
examples = classify_edges(lines)

# Plota o perfil das linhas de cada tipo de borda
plot_line_profiles(examples, "degrau")
plot_line_profiles(examples, "rampa")
plot_line_profiles(examples, "telhado")