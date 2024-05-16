import cherrypy
import json

class ChatServer:
    @cherrypy.expose
    def index(self):
        return """
            <html>
                <body>
                    <h1>Chat Application</h1>
                    <form action="send_message">
                        <input type="text" name="message" />
                        <button type="submit">Send</button>
                    </form>
                    <ul id="messages"></ul>
                    <script src="https://cdn.jsdelivr.net/npm/axios@0.21.1/dist/axios.min.js"></script>
                    <script>
                        function updateMessages() {
                            axios.get('get_messages')
                                .then(response => {
                                    const messages = response.data;
                                    const messagesList = document.getElementById('messages');
                                    messagesList.innerHTML = '';
                                    messages.forEach(message => {
                                        const messageElement = document.createElement('LI');
                                        messageElement.textContent = message;
                                        messagesList.appendChild(messageElement);
                                    });
                                })
                                .catch(error => console.error(error));
                        }

                        updateMessages();
                        setInterval(updateMessages, 1000);

                        const form = document.querySelector('form');
                        form.addEventListener('submit', event => {
                            event.preventDefault();
                            const messageInput = document.querySelector('input[name="message"]');
                            const message = messageInput.value.trim();
                            if (message) {
                                axios.post('send_message', { message })
                                    .then(() => messageInput.value = '')
                                    .catch(error => console.error(error));
                            }
                        });
                    </script>
                </body>
            </html>
        """

    @cherrypy.expose
    def send_message(self, message):
        # Add the message to the database or any other storage
        # For simplicity, we'll just store it in memory
        messages.append(message)
        return "Message sent successfully"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_messages(self):
        # Return all messages from the database or storage
        # Again, for simplicity, we'll just return the in-memory list
        return messages


if __name__ == '__main__':
    messages = []
    cherrypy.config.update({'server.socket_port': 8000})
    cherrypy.quickstart(ChatServer())