from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QProgressBar,
    QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from game import Hero, Devil

app = QApplication([])

class RPGGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔥 RPG: Hero vs Devil 🔥")
        self.setGeometry(350, 180, 540, 500)
        self.setStyleSheet("""
            QWidget { background:#1e1e2e; color:white; font-size:14px; }
            QPushButton {
                background:#ff5555;
                border-radius:10px;
                padding:10px;
                font-weight:bold;
            }
            QPushButton:hover { background:#ff7777; }
            QProgressBar {
                height:18px;
                border-radius:8px;
                background:#444;
            }
            QProgressBar::chunk {
                background:#ff5555;
                border-radius:8px;
            }
            QTextEdit { background:#111; border-radius:8px; }
        """)
        self.setup_game()
        self.setup_ui()
        self.update_ui()

    def setup_game(self):
        self.hero = Hero("Hero", 130, 18)
        self.devil = Devil("Devil", 150, 19)

    def setup_ui(self):
        title = QLabel("⚔ ISEKAI BATTLE ⚔")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:20px; font-weight:bold;")

        self.hero_hp = QProgressBar()
        self.hero_hp.setMaximum(self.hero.max_hp)
        self.devil_hp = QProgressBar()
        self.devil_hp.setMaximum(self.devil.max_hp)

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        self.btn_holy = QPushButton("🗡 Holy Blade")
        self.btn_frost = QPushButton("❄ Frost Dominion")
        self.btn_inferno = QPushButton("🔥 Inferno Cataclysm")
        self.btn_restart = QPushButton("🔄 Restart")

        self.btn_holy.clicked.connect(self.holy)
        self.btn_frost.clicked.connect(self.frost)
        self.btn_inferno.clicked.connect(self.inferno)
        self.btn_restart.clicked.connect(self.restart)

        hero_box = QVBoxLayout()
        hero_box.addWidget(QLabel("🛡 HERO"))
        hero_box.addWidget(self.hero_hp)

        devil_box = QVBoxLayout()
        devil_box.addWidget(QLabel("😈 DEVIL"))
        devil_box.addWidget(self.devil_hp)

        attacks = QHBoxLayout()
        attacks.addWidget(self.btn_holy)
        attacks.addWidget(self.btn_frost)
        attacks.addWidget(self.btn_inferno)

        main = QVBoxLayout()
        main.addWidget(title)
        main.addLayout(hero_box)
        main.addLayout(devil_box)
        main.addWidget(QLabel("📜 Battle Log"))
        main.addWidget(self.log)
        main.addLayout(attacks)
        main.addWidget(self.btn_restart)

        self.setLayout(main)

    def update_ui(self):
        self.hero_hp.setValue(max(self.hero.hp, 0))
        self.devil_hp.setValue(max(self.devil.hp, 0))

    def devil_turn(self):
        if self.devil.is_alive():
            self.log.append(self.devil.attack_enemy(self.hero))

    def holy(self):
        self.log.append(self.hero.holy_blade(self.devil))
        self.devil_turn()
        self.after_turn()

    def frost(self):
        self.log.append(self.hero.frost_dominion(self.devil))
        self.devil_turn()
        self.after_turn()

    def inferno(self):
        self.log.append(self.hero.inferno_cataclysm(self.devil))
        self.devil_turn()
        self.after_turn()

    def after_turn(self):
        self.check_game()
        self.update_ui()

    def check_game(self):
        if not self.hero.is_alive():
            QMessageBox.information(self, "Game Over", "💀 Hero perished")
            self.disable_buttons()
        elif not self.devil.is_alive():
            QMessageBox.information(self, "Victory", "🏆 Devil defeated!")
            self.disable_buttons()

    def disable_buttons(self):
        self.btn_holy.setEnabled(False)
        self.btn_frost.setEnabled(False)
        self.btn_inferno.setEnabled(False)

    def restart(self):
        self.setup_game()
        self.btn_holy.setEnabled(True)
        self.btn_frost.setEnabled(True)
        self.btn_inferno.setEnabled(True)
        self.log.clear()
        self.update_ui()


window = RPGGame()
window.show()
app.exec_()
