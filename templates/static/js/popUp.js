document.addEventListener('DOMContentLoaded', function() {
    // Получение элементов
    var modal = document.getElementById("authModal");
    var closeModalBtn = document.getElementById("closeModal");
    var loginForm = document.getElementById("loginForm");
    var registerForm = document.getElementById("registerForm");
    var openLoginBtn = document.getElementById("openLogin");
    var openRegisterBtn = document.getElementById("openRegister");

    // Открытие формы для входа
    openLoginBtn.addEventListener('click', function() {
        modal.style.display = "flex";
        loginForm.style.display = "flex";
        registerForm.style.display = "none";
    });

    // Открытие формы для регистрации
    openRegisterBtn.addEventListener('click', function() {
        modal.style.display = "flex";
        registerForm.style.display = "flex";
        loginForm.style.display = "none";
    });

    // Закрытие модального окна
    closeModalBtn.addEventListener('click', function() {
        modal.style.display = "none";
    });

    // Закрытие окна при клике за его пределы
    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
    function enableRoleCode() {
        var buildingCode = document.getElementById('buildingCode').value;
        var roleCodeField = document.getElementById('roleCode');
        
        if (buildingCode === '003') {
            roleCodeField.disabled = false;
        } else {
            roleCodeField.disabled = true;
            document.getElementById('role').value = '';
            roleCodeField.value = '';
        }
    }
    // Функция для установки роли на основе кода роли
    function setRole() {
        var roleCode = document.getElementById('roleCode').value;
        var roleField = document.getElementById('role');
        
        if (roleCode === '001') {
            roleField.value = 'Доктор';
        } else if (roleCode === '002') {
            roleField.value = 'Пациент';
        } else {
            roleField.value = '';
        }
    }

    // Функция для включения/отключения поля кода роли на основе кода здания
    

    // Привязка функции установки роли к событию ввода в поле кода роли
    document.getElementById('roleCode').addEventListener('input', setRole);

    // Привязка функции включения/отключения кода роли к событию ввода в поле кода здания
    document.getElementById('buildingCode').addEventListener('input', enableRoleCode);
});
