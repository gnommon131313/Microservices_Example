export function isTgWebApp() {
    // Проверка на запуск сайта внутри телеграма (через Mini Apps)(нужно т.к. нету кастомной регистрации а многие функции требую идентифицировать пользователя, например ID)
    if (window.Telegram && window.Telegram.WebApp) {
        let tg = window.Telegram.WebApp;
        const user = tg.initDataUnsafe.user;

        if (user) {
            alert(user.id);
            return true;
        } else {
            alert('user data is empty');
            return false;
        }
    } else {
        alert('WebApp not found');
        return false;
    }
}
