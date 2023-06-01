<template>
    <div>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="  ">{{ test.name }}</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
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
                        <Sample v-if="item.generator_id == 1" :item="item" @answered="saveAnswer" />
                        <InvGraph v-if="item.generator_id == 2" :item="item" @answered="saveAnswer" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { compile } from 'vue';
import Sample from '../components/generators/sample.vue'
import InvGraph from '../components/generators/inv_graph.vue'
import axios from 'axios';

export default {
    components: {
        Sample,
        InvGraph,
    },
    data() {
        return {
            user: {
                id: '1',
                fullname: 'Суханов Егор Алексеевич',
            },
            test: {
                left_time: 2,
            },
            activeItem: 1,
            items: [
                {
                    id: '1',
                    short_name: "1",
                    generator_id: 0,
                    public_data: {
                        question: "Даны высказывания:<br>1) То, что N делится на 15, есть необходимое условие того, чтобы N делилось на 3.<br>2) То, что N не делится на 3, влечёт то, что N не делится на 15.<br>3) N делится на 3 при условии, что N делится на 15.<br>4) N не делится на 3 только тогда, когда N не делится на 15.<br>5) N делится на 3 тогда и только тогда, когда N делится на 15.<br>Какие из них следуют из высказывания N делится на 15, то N делится на 3?<br>",
                        checks: [
                            { id: "1", text: "1" },
                            { id: "2", text: "2" },
                            { id: "3", text: "3" },
                            { id: "4", text: "4" },
                            { id: "5", text: "5" },
                        ],
                    },
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
            answers: {

            },
        }
    },
    methods: {
        isActive(menuItem) {
            return this.activeItem === menuItem
        },
        setActive(menuItem) {
            this.activeItem = menuItem
        },
        getTasks() {
            let test_id = this.$route.params.id

            function calculateDurationInSeconds(end_time) {
                const startTime = Date.now();
                const endTime = new Date(end_time);
                const shift = 3600 * 3;

                // Разница в миллисекундах между двумя моментами времени
                const timeDiff = endTime - startTime;

                // Перевод разницы в миллисекундах в секунды
                const durationInSeconds = Math.floor(timeDiff / 1000 + shift);

                return durationInSeconds;
            }

            console.log(test_id)
            axios
                .get("/student/test/" + test_id)
                .then(response => {
                    this.test = response.data.test;
                    this.items = response.data.items;
                    this.activeItem = this.items[0].id;
                    this.test.left_time = calculateDurationInSeconds(this.test.end_time);
                    console.log(response.data)
                });
        },
        saveAnswer(answer) {
            console.log(answer)
            let test_id = this.$route.params.id

            this.answers[this.activeItem] = JSON.stringify(answer)
            axios
                .put('student/test/' + test_id + '/' + this.activeItem, { answer: this.answers[this.activeItem] })
        },
    },
    beforeMount() {
        this.getTasks();
    }
}
</script>