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
                <div class="modal" tabindex="-1" id="createInstance" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Создание экземпляра</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="datepicker-container">
                                    <label for="date" class="form-label">Время начала:</label><br>
                                    <input type="date" name="date">
                                </div>
                                <label for=" date" class="form-label">Длительность:</label>
                                <div class="cs-form">
                                    <input type="time" class="form-control" value="10:05 AM" />
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отмена</button>
                                <button type="button" class="btn btn-primary">Создать</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Scrollable modal -->
                <div class="modal fade modal-xl" id="createTemplateModal" tabindex="-1"
                    aria-labelledby="createTemplateModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="createTemplateModalLabel">{{ new_template.name }}
                                </h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="">
                                <input v-model="new_template.name" type="text" class="form-control" id="floatingInput"
                                    placeholder="Название шаблона">
                                <button type="button" class="btn btn-sm btn-secondary m-3"
                                    @click="createTemplateAddBlock()"> Добавить блок задач </button>
                            </div>
                            <div>
                                <div class=" modal-body">
                                    <div class="card" v-for=" block  in   new_template.blocks  "
                                        :key="'block_' + block.block_number">
                                        <h5 class="card-header">{{ block.name }}</h5>
                                        <div class="card-body">
                                            <input v-model="block.name" type="text" class="form-control mb-3"
                                                id="floatingInput" placeholder="Название Группы заданий">
                                            {{ block.selected }}
                                            <select class="form-select mb-3" aria-label="Default select example"
                                                v-model="block.selected">
                                                <option selected>Выбрать генератор</option>
                                                <option v-for=" generator  in  generators " :value="generator.id">{{
                                                    generator.name }}</option>
                                            </select>
                                            <div class="mb-3">
                                                <label for="formFile" class="form-label">Json настройки
                                                    генератора:</label>
                                                <input class="form-control" type="file"
                                                    @change="createtemplateReadFile($event.target.files[0], block)">
                                                Текст для отладки: {{ block.config }}
                                            </div>
                                            <button type="button" class="btn btn-sm btn-danger m-1"
                                                @click="createTemplateRemoveBlock(block)">Удалить</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary btn-sm"
                                    data-bs-dismiss="modal">Закрыть</button>
                                <button type="button" class="btn btn-primary btn-sm" @click="createTemplateSave"
                                    data-bs-dismiss="modal">Сохранить</button>
                            </div>
                        </div>
                    </div>
                </div>
                <button type="button" class="btn btn-sm btn-primary m-1" data-bs-toggle="modal"
                    data-bs-target="#createTemplateModal">Создать тест</button>
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center"
                        v-for="  template   in   templates  " :key="'template_' + template.id">
                        <span>{{ template.name }}</span>
                        <div>
                            <button type="button" class="btn btn-sm btn-success m-1" data-bs-toggle="modal"
                                data-bs-target="#createInstance">Запустить</button>
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
                        v-for="  generator   in   generators  " :key="'template_' + generator.id">
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
import axios from 'axios'
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
                    status: "Запущен",
                    start: "01:40:00 20.04.2023",
                    end: "02:40:00 20.04.2023",
                    duration: "1:00:00",
                },
                {
                    id: "2",
                    name: "Тест 2",
                    status: "Завершен",
                    start: "00:00:00 20.05.2023",
                    end: "01:30:00 20.05.2023",
                    duration: "1:30:00",
                }
            ],
            templates: [
                {
                    id: "1",
                    name: "Тест 1",
                },
                // {
                //     id: "2",
                //     name: "Тест 2",
                // },
                // {
                //     id: "3",
                //     name: "Тест 3",
                // }
            ],
            new_template: {
                name: "",
                blocks: [
                    {
                        name: "",
                        generator_id: 0,
                        block_number: 0,
                        config: "",
                    }
                ]
            },
            generators: [
                {
                    id: 0,
                    name: "Текстовый генератор",
                }
            ]
        }
    },
    methods: {
        get_templates() {
            axios
                .get('/admin/templates')
                .then(response => { this.templates = response.data; console.log(response.data) });
        },
        post_template() {

        },
        get_template_blocks() {

        },

        createTemplateRemoveBlock(block) {
            let indexToRemove = this.new_template.blocks.findIndex(b => b.name === block.name);
            this.new_template.blocks.splice(indexToRemove)
        },
        // TODO block_number изменить, там баг есть
        createTemplateAddBlock() {
            this.new_template.blocks.push({
                name: "",
                generator_id: 0,
                block_number: this.new_template.blocks.length,
                config: "",
            })
        },
        createtemplateReadFile(file, block) {
            // const file = file;
            const reader = new FileReader();

            reader.onload = () => {
                try {
                    const content = JSON.parse(reader.result);
                    console.log(content);
                    // Ваш код для работы с содержимым JSON-файла
                    block.config = JSON.stringify(content);
                } catch (error) {
                    console.error("Ошибка чтения JSON-файла:", error);
                }
            };

            reader.readAsText(file);
        },
        createTemplateSave() {
            // Запрос
            axios.post('/admin/templates', this.new_template)
                .then(res => {
                    console.log(res)
                })
            // А потом сбросить new_template

        },
    },
    beforeMount() {
        this.get_templates()
    }
}
</script>


<style scoped></style>