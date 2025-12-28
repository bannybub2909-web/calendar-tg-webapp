const tg = window.Telegram.WebApp;
tg.expand();

function sendData() {
  const date = document.getElementById("date").value;
  const text = document.getElementById("text").value;

  if (!date) {
    tg.showAlert("Выберите дату");
    return;
  }

  tg.sendData(JSON.stringify({
    date: date,
    text: text
  }));

  tg.close();
}
