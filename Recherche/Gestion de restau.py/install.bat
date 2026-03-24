@echo off
echo Installation du système de gestion de restaurant
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installé. Veuillez installer Python 3.8+
    pause
    exit /b 1
)

REM Installer les dépendances
echo Installation des dépendances...
pip install mysql-connector-python python-dotenv

REM Créer la base de données
echo.
echo Création de la base de données...
mysql -u root -p < restaurant.sql

echo.
echo Installation terminée!
echo Pour démarrer: python main.py
pause