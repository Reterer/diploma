<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Тест 1</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="badge bg-secondary">
                Осталось времени: 13:45
            </div>
            <div>
                <div>
                    Суханов Егор алексеевич
                </div>
                <button type="button" class="btn btn-secondary btn-sm">Завершить</button>
            </div>
        </div>
    </nav>
    <div class="container" style="margin-top: 40px;">
        <div class="d-flex align-items-start">
            <ul class="nav flex-column nav-pills me-3">
                <li class="nav-item">
                    <a class="nav-link" @click.prevent="setActive('home')" :class="{ active: isActive('home') }"
                        href="#home">1</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click.prevent="setActive('profile')" :class="{ active: isActive('profile') }"
                        href="#profile">2</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click.prevent="setActive('contact')" :class="{ active: isActive('contact') }"
                        href="#contact">3</a>
                </li>
            </ul>
            <div class="tab-content py-3" id="myTabContent">
                <div class="tab-pane fade" :class="{ 'active show': isActive('home') }" id="home">1</div>
                <div class="tab-pane fade" :class="{ 'active show': isActive('profile') }" id="profile">2
                </div>
                <div class="tab-pane fade" :class="{ 'active show': isActive('contact') }" id="contact">3
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            activeItem: 'home',
            items: [

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