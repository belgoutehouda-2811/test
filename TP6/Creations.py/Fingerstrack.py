import cv2
import mediapipe as mp

# Initialiser MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# Démarrer la capture vidéo
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Erreur de capture vidéo")
        continue

    # Convertir l'image en RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Traiter l'image avec MediaPipe
    results = hands.process(image_rgb)

    # Convertir l'image en BGR pour l'affichage
    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    # Dessiner les landmarks des mains
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
            )

    # Afficher le résultat
    cv2.imshow('Finger Tracker', image)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()