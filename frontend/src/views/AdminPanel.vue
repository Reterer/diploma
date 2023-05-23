<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Панель управления</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="">
                <div>
                    {{ user.fullname }}
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
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center"
                        v-for="instance in instances" :key="'instance_' + instance.id">
                        <div class="d-flex justify-content-between">
                            <div class="m-1 badge text-bg-info">{{ instance.name }}</div>
                            <div class="m-1 badge text-bg-secondary">{{ instance.status }}</div>
                            <div class="m-1 badge text-bg-secondary">Старт: {{ instance.start }}</div>
                            <div class="m-1 badge text-bg-secondary">Конец: {{ instance.end }}</div>
                            <div class="m-1 badge text-bg-secondary">Длительность: {{ instance.duration }}</div>
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
                    <li class="list-group-item d-flex justify-content-between align-items-center"
                        v-for="template in templates" :key="'template_' + template.id">
                        <span>{{ template.name }}</span>
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
                </ul>
            </div>
            <div class="tab-pane fade" style="margin-top: 10px;" id="contact-tab-pane" role="tabpanel"
                aria-labelledby="contact-tab" tabindex="0">
                <!-- <button type="button" class="btn btn-sm btn-primary m-1">Добавить генератор</button> -->
                <!-- Генераторы -->
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center"
                        v-for="generator in generators" :key="'template_' + generator.id">
                        <span>{{ generator.name }}</span>
                        <div>
                            <!-- <button type="button" class="btn btn-sm btn-danger m-1">Удалить</button> -->
                        </div>

                    </li>
                </ul>
            </div>
        </div>


    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                id: '1',
                fullname: "Фамилия Имя Отчество",
            },
            instances: [
                {
                    id: "1",
                    name: "Тест 1",
                    status: "Завершен",
                    start: "23:23:15 19.04.2023",
                    end: "00:23:15 20.04.2023",
                    duration: "1:00:00",
                },
                {
                    id: "2",
                    name: "Тест 2",
                    status: "Запущен",
                    start: "00:00:00 20.04.2023",
                    end: "1:30:00 20.04.2023",
                    duration: "40:35",
                }
            ],
            templates: [
                {
                    id: "1",
                    name: "Тест 1",
                },
                {
                    id: "2",
                    name: "Тест 2",
                },
                {
                    id: "3",
                    name: "Тест 3",
                }
            ],
            generators: [
                {
                    id: "1",
                    name: "Текстовый генератор",
                }
            ]
        }
    },
}
</script>


<style scoped></style>