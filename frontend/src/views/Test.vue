<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">{{ test.name }}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="badge bg-secondary">
                Осталось времени: {{ test.left_time }}
            </div>
            <div>
                <div>
                    {{ user.fullname }}
                </div>
                <button type="button" class="btn btn-secondary btn-sm">Завершить</button>
            </div>
        </div>
    </nav>
    <div class="container" style="margin-top: 40px;">
        <div class="d-flex align-items-start">
            <ul class="nav flex-column nav-pills me-3">
                <li class="nav-item" v-for="item in items" :key="'item_nav_' + item.id">
                    <a class="nav-link" @click.prevent="setActive(item.id)" :class="{ active: isActive(item.id) }"
                        href="#1">{{ item.short_name }}</a>
                </li>
            </ul>
            <div class="tab-content py-3" id="myTabContent">
                <div v-for="item in items" :key="'item_div_' + item.id" class="tab-pane fade container"
                    :class="{ 'active show': isActive(item.id) }" :id="'item_div_' + item.id">
                    <!-- {{ item.answer }} -->
                    <div>
                        <h4>Вопрос:</h4>
                        {{ item.question }}
                    </div>
                    <h4>Варианты ответа:</h4>
                    <div class="form-check" v-for="check in item.checks">
                        <input class="form-check-input" type="checkbox" :value="check.id" v-model="item.answer">
                        <label class="form-check-label">
                            {{ check.text }}
                        </label>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { compile } from 'vue';

export default {
    data() {
        return {
            user: {
                id: '1',
                fullname: 'Суханов Егор Алексеевич',
            },
            test: {
                id: '1',
                name: "Тест 1",
                left_time: "13:45",
            },
            activeItem: '1',
            items: [
                {
                    id: '1',
                    short_name: "1",
                    question: "Текстовая форма вопроса",
                    checks: [
                        {
                            id: "0",
                            text: "Первый ответ"
                        },
                        {
                            id: "1",
                            text: "Второй ответ"
                        },
                        {
                            id: "2",
                            text: "Третий ответ"
                        },
                        {
                            id: "3",
                            text: "Четвертый ответ"
                        },
                    ],
                    answer: [],
                },
                {
                    id: '2',
                    short_name: "2",
                    body: "test 2",
                },
                {
                    id: '3',
                    short_name: "3",
                    body: "test 3",
                },
                {
                    id: '4',
                    short_name: "4",
                    body: "test 4",
                }
            ],
        }
    },
    methods: {
        isActive(menuItem) {
            return this.activeItem === menuItem
        },
        setActive(menuItem) {
            this.activeItem = menuItem
        }
    }
}
</script>