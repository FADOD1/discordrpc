import flet as ft
from pypresence import Presence
import time
import threading

# Versão da aplicação
VERSION = "1.0.0"

class DiscordRichPresenceApp:
    def __init__(self):
        self.presence = None
        self.running = False

    def start_presence(self, client_id, state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image):
        self.presence = Presence(client_id)
        self.presence.connect()
        self.running = True

        while self.running:
            presence_data = {}
            if show_state:
                presence_data["state"] = state
            if show_details:
                presence_data["details"] = details
            if show_large_image:
                presence_data["large_image"] = large_image
            if show_small_image:
                presence_data["small_image"] = small_image

            presence_data.update(
                start=start_time
            )

            self.presence.update(**presence_data)
            time.sleep(15)  # Atualiza a cada 15 segundos

    def stop_presence(self):
        self.running = False
        if self.presence:
            self.presence.close()

    def update_presence(self, state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image):
        if self.presence:
            presence_data = {}
            if show_state:
                presence_data["state"] = state
            if show_details:
                presence_data["details"] = details
            if show_large_image:
                presence_data["large_image"] = large_image
            if show_small_image:
                presence_data["small_image"] = small_image

            presence_data.update(
                start=start_time
            )
            self.presence.update(**presence_data)

def main(page: ft.Page):
    page.title = f"Rich Presence para Discord - v{VERSION}"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Variável de status
    status_text = ft.Text("")

    # Funções para controlar o Rich Presence
    app = DiscordRichPresenceApp()

    def start_rich_presence(e):
        client_id = txt_client_id.value
        state = txt_state.value
        details = txt_details.value
        large_image = txt_large_image.value
        small_image = txt_small_image.value
        start_time = int(time.time()) if chk_start_time.value else None
        show_state = chk_show_state.value
        show_details = chk_show_details.value
        show_large_image = chk_show_large_image.value
        show_small_image = chk_show_small_image.value

        # Validação para garantir que o Client ID foi inserido
        if not client_id:
            status_text.value = "Por favor, insira o Client ID."
            status_text.color = ft.colors.RED
            page.update()
            return

        # Inicia a thread para atualizar o Rich Presence
        threading.Thread(
            target=app.start_presence,
            args=(client_id, state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image),
            daemon=True
        ).start()
        
        # Atualiza o status de execução
        status_text.value = "Rich Presence em execução!"
        status_text.color = ft.colors.GREEN
        page.update()

    def stop_rich_presence(e):
        app.stop_presence()
        # Atualiza o status de parada
        status_text.value = "Rich Presence parado."
        status_text.color = ft.colors.RED
        page.update()

    def update_rich_presence(e):
        state = txt_state.value
        details = txt_details.value
        large_image = txt_large_image.value
        small_image = txt_small_image.value
        start_time = int(time.time()) if chk_start_time.value else None
        show_state = chk_show_state.value
        show_details = chk_show_details.value
        show_large_image = chk_show_large_image.value
        show_small_image = chk_show_small_image.value

        # Atualiza o Rich Presence com as novas informações
        app.update_presence(state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image)

        # Atualiza o status
        status_text.value = "Rich Presence atualizado!"
        status_text.color = ft.colors.BLUE
        page.update()

    # Campo para inserir o Client ID
    txt_client_id = ft.TextField(label="Client ID", width=300)
    txt_state = ft.TextField(label="Estado", width=300)
    txt_details = ft.TextField(label="Detalhes", width=300)
    txt_large_image = ft.TextField(label="Imagem Grande (ID)", width=300)
    txt_small_image = ft.TextField(label="Imagem Pequena (ID)", width=300)
    chk_start_time = ft.Checkbox(label="Iniciar com timestamp")

    # Checkboxes para mostrar ou não as informações
    chk_show_state = ft.Checkbox(label="Mostrar Estado", value=True)
    chk_show_details = ft.Checkbox(label="Mostrar Detalhes", value=True)

    # Checkboxes para as imagens
    chk_show_large_image = ft.Checkbox(label="Mostrar Imagem Grande", value=True)
    chk_show_small_image = ft.Checkbox(label="Mostrar Imagem Pequena", value=True)

    # Layout da página
    page.add(
        txt_client_id,
        txt_state,
        txt_details,
        txt_large_image,
        txt_small_image,
        chk_start_time,
        chk_show_state,
        chk_show_details,
        chk_show_large_image,
        chk_show_small_image,
        ft.Row(
            [
                ft.ElevatedButton("Iniciar Rich Presence", on_click=start_rich_presence),
                ft.ElevatedButton("Parar Rich Presence", on_click=stop_rich_presence),
                #ft.ElevatedButton("Atualizar Rich Presence", on_click=update_rich_presence),  # Botão para atualizar
                ft.ElevatedButton("Atuakizar o Rich Presence", on_click=update_rich_presence), 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        status_text
    )

ft.app(target=main, assets_dir="assets")
import flet as ft
from pypresence import Presence
import time
import threading

# Versão da aplicação
VERSION = "1.0.0"

class DiscordRichPresenceApp:
    def __init__(self):
        self.presence = None
        self.running = False

    def start_presence(self, client_id, state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image):
        try:
            self.presence = Presence(client_id)
            self.presence.connect()
            self.running = True

            while self.running:
                presence_data = {}
                if show_state:
                    presence_data["state"] = state
                if show_details:
                    presence_data["details"] = details
                if show_large_image:
                    presence_data["large_image"] = large_image
                if show_small_image:
                    presence_data["small_image"] = small_image

                presence_data.update(start=start_time)

                self.presence.update(**presence_data)
                time.sleep(15)  # Atualiza a cada 15 segundos
        except Exception as e:
            print(f"Erro no Rich Presence: {e}")

    def stop_presence(self):
        self.running = False
        if self.presence:
            self.presence.close()

    def update_presence(self, state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image):
        if self.presence:
            try:
                presence_data = {}
                if show_state:
                    presence_data["state"] = state
                if show_details:
                    presence_data["details"] = details
                if show_large_image:
                    presence_data["large_image"] = large_image
                if show_small_image:
                    presence_data["small_image"] = small_image

                presence_data.update(start=start_time)
                self.presence.update(**presence_data)
            except Exception as e:
                print(f"Erro ao atualizar Rich Presence: {e}")

def main(page: ft.Page):
    page.title = f"Rich Presence para Discord - v{VERSION}"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Comportamento para minimizar/restaurar janela
    page.on_window_event = lambda e: page.window_restore() if e.data == "restore" else None

    # Variável de status
    status_text = ft.Text("")

    # Inicializa o controlador do Rich Presence
    app = DiscordRichPresenceApp()

    def start_rich_presence(e):
        client_id = txt_client_id.value
        state = txt_state.value
        details = txt_details.value
        large_image = txt_large_image.value
        small_image = txt_small_image.value
        start_time = int(time.time()) if chk_start_time.value else None
        show_state = chk_show_state.value
        show_details = chk_show_details.value
        show_large_image = chk_show_large_image.value
        show_small_image = chk_show_small_image.value

        # Validação do Client ID
        if not client_id:
            status_text.value = "Por favor, insira o Client ID."
            status_text.color = ft.colors.RED
            page.update()
            return

        # Inicia a thread para o Rich Presence
        threading.Thread(
            target=app.start_presence,
            args=(client_id, state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image),
            daemon=True
        ).start()
        status_text.value = "Rich Presence em execução!"
        status_text.color = ft.colors.GREEN
        page.update()

    def stop_rich_presence(e):
        app.stop_presence()
        status_text.value = "Rich Presence parado."
        status_text.color = ft.colors.RED
        page.update()

    def update_rich_presence(e):
        state = txt_state.value
        details = txt_details.value
        large_image = txt_large_image.value
        small_image = txt_small_image.value
        start_time = int(time.time()) if chk_start_time.value else None
        show_state = chk_show_state.value
        show_details = chk_show_details.value
        show_large_image = chk_show_large_image.value
        show_small_image = chk_show_small_image.value

        # Atualiza o Rich Presence
        app.update_presence(state, details, large_image, small_image, start_time, show_state, show_details, show_large_image, show_small_image)
        status_text.value = "Rich Presence atualizado!"
        status_text.color = ft.colors.BLUE
        page.update()

    # Componentes de entrada
    txt_client_id = ft.TextField(label="Client ID", width=300)
    txt_state = ft.TextField(label="Estado", width=300)
    txt_details = ft.TextField(label="Detalhes", width=300)
    txt_large_image = ft.TextField(label="Imagem Grande (ID)", width=300)
    txt_small_image = ft.TextField(label="Imagem Pequena (ID)", width=300)
    chk_start_time = ft.Checkbox(label="Iniciar com timestamp")

    # Checkboxes para mostrar ou não informações
    chk_show_state = ft.Checkbox(label="Mostrar Estado", value=True)
    chk_show_details = ft.Checkbox(label="Mostrar Detalhes", value=True)
    chk_show_large_image = ft.Checkbox(label="Mostrar Imagem Grande", value=True)
    chk_show_small_image = ft.Checkbox(label="Mostrar Imagem Pequena", value=True)

    # Layout da página
    page.add(
        txt_client_id,
        txt_state,
        txt_details,
        txt_large_image,
        txt_small_image,
        chk_start_time,
        chk_show_state,
        chk_show_details,
        chk_show_large_image,
        chk_show_small_image,
        ft.Row(
            [
                ft.ElevatedButton("Iniciar Rich Presence", on_click=start_rich_presence),
                ft.ElevatedButton("Parar Rich Presence", on_click=stop_rich_presence),
                #sft.ElevatedButton("Atualizar Rich Presence", on_click=update_rich_presence),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        status_text
    )

ft.app(target=main, assets_dir="assets")
