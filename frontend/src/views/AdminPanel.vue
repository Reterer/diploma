<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Панель управления</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <!-- <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                            aria-expanded="false">
                            Dropdown
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled">Disabled</a>
                    </li>
                </ul>
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div> -->
            <div class="">
                <div>
                    Суханов Егор алексеевич
                </div>
                <button type="button" class="btn btn-secondary btn-sm">Выход</button>
            </div>
        </div>
    </nav>

    <div>
        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane"
                    type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Экземпляры тестов</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane"
                    type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Шаблоны тестов</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane"
                    type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false">Генераторы</button>
            </li>
        </ul>
        <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" style="margin-top: 10px;" id="home-tab-pane" role="tabpanel"
                aria-labelledby="home-tab" tabindex="0">
                <!-- Экземпляры тестов -->
                <!-- <div class="card">
                    <div class="card-header">
                        Featured
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Special title treatment</h5>
                        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div> -->

                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div class="d-flex justify-content-between">
                            <div class="m-1 badge text-bg-info">Тест 1</div>
                            <div class="m-1 badge text-bg-secondary">Завершен</div>
                            <div class="m-1 badge text-bg-secondary">Старт: 23:23:15 19.05.2023</div>
                            <div class="m-1 badge text-bg-secondary">Конец: 24:23:15</div>
                            <div class="m-1 badge text-bg-secondary">Длительность: 1:00:00</div>
                        </div>
                        <div>
                            <button type="button" class="btn btn-sm btn-secondary m-1">Выгрузить материалы</button>
                            <button type="button" class="btn btn-sm btn-secondary m-1">Выгрузить таблицу</button>
                            <button type="button" class="btn btn-sm btn-secondary m-1">Подробнее</button>
                            <button type="button" class="btn btn-sm btn-danger m-1">Удалить</button>
                        </div>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div class="d-flex justify-content-between">
                            <div class="m-1 badge text-bg-info">Тест 2</div>
                            <div class="m-1 badge text-bg-secondary">Идет</div>
                            <div class="m-1 badge text-bg-secondary">Старт: 23:23:15 19.05.2023</div>
                            <div class="m-1 badge text-bg-secondary">Конец: 24:23:15</div>
                            <div class="m-1 badge text-bg-secondary">Осталось времени: 0:40:17</div>
                        </div>
                        <div>
                            <button type="button" class="btn btn-sm btn-secondary m-1">Выгрузить материалы</button>
                            <button type="button" class="btn btn-sm btn-secondary m-1">Выгрузить таблицу</button>
                            <button type="button" class="btn btn-sm btn-secondary m-1">Подробнее</button>
                            <button type="button" class="btn btn-sm btn-danger m-1">Удалить</button>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="tab-pane fade" style="margin-top: 10px;" id="profile-tab-pane" role="tabpanel"
                aria-labelledby="profile-tab" tabindex="0">
                <!-- Шаблоны тестов -->
                <!-- Button trigger modal -->


                <!-- Modal -->
                <!-- Scrollable modal -->
                <div class="modal fade modal-xl" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel"
                    aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Тест 1</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="">
                                <button type="button" class="btn btn-sm btn-secondary m-3">Добавить блок задач</button>
                            </div>
                            <div>
                                <div class="modal-body">
                                    <div class="card">
                                        <h5 class="card-header">Блок задач 1</h5>
                                        <div class="card-body">
                                            <h5 class="card-title">Генератор</h5>
                                            <p class="card-text">Какие-то настройки генератора</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary btn-sm"
                                    data-bs-dismiss="modal">Закрыть</button>
                                <button type="button" class="btn btn-primary btn-sm">Сохранить</button>
                            </div>
                        </div>
                    </div>
                </div>
                <button type="button" class="btn btn-sm btn-primary m-1">Создать тест</button>
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <span>Тест 1</span>
                        <div>
                            <button type="button" class="btn btn-sm btn-success m-1">Запустить</button>
                            <!-- <button type="button" class="btn btn-sm btn-primary m-1">Изменить</button> -->
                            <button type="button" class="btn btn-primary btn-sm m-1" data-bs-toggle="modal"
                                data-bs-target="#exampleModal">
                                Изменить
                            </button>
                            <button type="button" class="btn btn-sm btn-danger m-1">Удалить</button>
                        </div>

                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <span>Тест 2</span>
                        <div>
                            <button type="button" class="btn btn-sm btn-success m-1">Запустить</button>
                            <button type="button" class="btn btn-sm btn-primary m-1">Изменить</button>
                            <button type="button" class="btn btn-sm btn-danger m-1">Удалить</button>
                        </div>

                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <span>Тест 3</span>
                        <div>
                            <button type="button" class="btn btn-sm btn-success m-1">Запустить</button>
                            <button type="button" class="btn btn-sm btn-primary m-1">Изменить</button>
                            <button type="button" class="btn btn-sm btn-danger m-1">Удалить</button>
                        </div>

                    </li>
                </ul>
            </div>
            <div class="tab-pane fade" style="margin-top: 10px;" id="contact-tab-pane" role="tabpanel"
                aria-labelledby="contact-tab" tabindex="0">
                <button type="button" class="btn btn-sm btn-primary m-1">Добавить генератор</button>
                <!-- Генераторы -->
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <span>Текстовый шаблон</span>
                        <div>
                            <button type="button" class="btn btn-sm btn-danger m-1">Удалить</button>
                        </div>

                    </li>
                </ul>
            </div>
        </div>


    </div>
</template>

<script>

</script>


<style scoped></style>