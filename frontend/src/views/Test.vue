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
                    <div v-html="item.question">
                    </div>
                    <div>
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
                left_time: "58:45",
            },
            activeItem: '1',
            items: [
                {
                    id: '1',
                    short_name: "1",
                    question: "Даны высказывания:<br>1) То, что N делится на 15, есть необходимое условие того, чтобы N делилось на 3.<br>2) То, что N не делится на 3, влечёт то, что N не делится на 15.<br>3) N делится на 3 при условии, что N делится на 15.<br>4) N не делится на 3 только тогда, когда N не делится на 15.<br>5) N делится на 3 тогда и только тогда, когда N делится на 15.<br>Какие из них следуют из высказывания N делится на 15, то N делится на 3?<br>",
                    checks: [
                        {
                            id: "0",
                            text: "1"
                        },
                        {
                            id: "1",
                            text: "2"
                        },
                        {
                            id: "2",
                            text: "3"
                        },
                        {
                            id: "3",
                            text: "4"
                        },
                        {
                            id: "4",
                            text: "5"
                        }
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